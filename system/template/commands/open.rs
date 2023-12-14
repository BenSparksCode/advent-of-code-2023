use std::process::Command;

use crate::Day;

pub fn handle(day: Day) {
    let day_str = day.into_inner().to_string();

    let status = Command::new("bash")
        .arg("./open_day_files.sh")  // Path to your Bash script
        .arg(day_str)
        .status()
        .expect("Failed to execute open_files script");

    if !status.success() {
        eprintln!("Failed to open files for day {}", day.into_inner());
    }
}