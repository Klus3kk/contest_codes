use std::fs::File;
use std::io::{self, BufRead};

fn find_first_and_last_number(line: &str) -> (Option<u32>, Option<u32>) {
    let mut first_number: Option<u32> = None;
    let mut last_number: Option<u32> = None;

    for c in line.chars() {
        if c.is_digit(10) {
            let digit = c.to_digit(10).unwrap();

            if first_number.is_none() {
                first_number = Some(digit);
            }

            last_number = Some(digit);
        }
    }

    (first_number, last_number)
}

fn main() -> io::Result<()> {
    // Replace "input.txt" with the actual path to your file
    let file_path = "input.txt";
    let file = File::open(file_path)?;
    let mut sum = 0;
    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;

        let (first, last) = find_first_and_last_number(&line);

        if let (Some(first), Some(last)) = (first, last) {
            sum += 10 * first + last;
        }
    }

    println!("{}", sum);
    Ok(())
}
