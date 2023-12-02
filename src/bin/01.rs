advent_of_code::solution!(1);

pub fn part_one(input: &str) -> Option<u32> {
    let mut total: u32 = 0;

    for line in input.lines() {
        let mut first_num: u32 = 0;
        let mut last_num: u32 = 0;

        for c in line.chars() {
            if c.is_ascii_digit() {
                // Convert char to u32 using base 10
                last_num = c.to_digit(10).unwrap();
                if first_num == 0 {
                    first_num = c.to_digit(10).unwrap();
                }
            }
        }

        total += (first_num * 10) + last_num;
    }

    Some(total)
}

pub fn part_two(input: &str) -> Option<u32> {
    // replace num words e.g. one1one
    // Use part 1 algo
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
