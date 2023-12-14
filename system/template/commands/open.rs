use std::process::Command;
use crate::Day;

pub fn handle(day: Day, year: Option<u32>) {
    let day_str = day.into_inner().to_string();
    let year_str = year.map_or_else(|| chrono::Utc::now().format("%Y").to_string(), |y| y.to_string());

    let status = Command::new("bash")
        .arg("./system/open_day_files.sh")
        .arg(day_str)
        .arg(&year_str)
        .status()
        .expect("Failed to execute open_files script");

    if !status.success() {
        eprintln!("Failed to open files for day {} of year {}", day.into_inner(), year_str);
    }
}