use std::{
    fs::{File, OpenOptions},
    io::Write,
    process,
};
use chrono::Datelike;
use crate::Day;

const MODULE_TEMPLATE: &str = r#"advent_of_code::solution!(DAY_NUMBER);

pub fn part_one(input: &str) -> Option<u32> {
    None
}

pub fn part_two(input: &str) -> Option<u32> {
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
"#;

// Create an additional .py file for a Python solution along with each Rust solution
const PYTHON_MODULE_TEMPLATE: &str = r#"# Advent of Code YEAR - Day DAY_NUMBER

def part_one(input):
    return None

def part_two(input):
    return None

if __name__ == "__main__":
    with open(f"data/YEAR/inputs/DAY.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))
"#;

fn safe_create_file(path: &str) -> Result<File, std::io::Error> {
    OpenOptions::new().write(true).create_new(true).open(path)
}

fn create_file(path: &str) -> Result<File, std::io::Error> {
    OpenOptions::new().write(true).create(true).open(path)
}

pub fn handle(day: Day, year: Option<u32>) {
    let year = year.unwrap_or_else(|| chrono::Utc::now().year() as u32);

    let input_path = format!("data/{year}/inputs/{:02}.txt", day.into_inner());
    let module_path = format!("{year}/Rust/{:02}.rs", day.into_inner());
    let python_module_path = format!("{year}/Python/{:02}.py", day.into_inner());


    let mut file = match safe_create_file(&module_path) {
        Ok(file) => file,
        Err(e) => {
            eprintln!("Failed to create module file: {e}");
            process::exit(1);
        }
    };

    match file.write_all(
        MODULE_TEMPLATE
            .replace("DAY_NUMBER", &day.into_inner().to_string())
            .as_bytes(),
    ) {
        Ok(()) => {
            println!("Created Rust module file \"{}\"", &module_path);
        }
        Err(e) => {
            eprintln!("Failed to write module contents: {e}");
            process::exit(1);
        }
    }

    // Additional code to handle creating the Python solution file
    let mut python_file = match safe_create_file(&python_module_path) {
        Ok(file) => file,
        Err(e) => {
            eprintln!("Failed to create Python module file: {e}");
            process::exit(1);
        }
    };

    match python_file.write_all(
        PYTHON_MODULE_TEMPLATE
            .replace("DAY_NUMBER", &day.into_inner().to_string())
            .replace("DAY", &day.to_string())
            .replace("YEAR", &year.to_string())
            .as_bytes(),
    ) {
        Ok(()) => {
            println!("Created Python module file \"{}\"", &python_module_path);
        }
        Err(e) => {
            eprintln!("Failed to write Python module contents: {e}");
            process::exit(1);
        }
    }
    // End of additional code

    match create_file(&input_path) {
        Ok(_) => {
            println!("Created empty input file \"{}\"", &input_path);
        }
        Err(e) => {
            eprintln!("Failed to create input file: {e}");
            process::exit(1);
        }
    }

    println!("---");
    println!("🎄 Type `cargo solve {}` to run your solution.", day);
}
