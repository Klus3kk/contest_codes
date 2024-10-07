use std::fs;

use regex::Regex;

#[derive(Debug)]
struct Pair {
    first: u32,
    last: u32,
}

trait PairTrait {
    fn result(&self) -> u32;
}

impl PairTrait for Pair {
    fn result(&self) -> u32 {
        self.first * 10 + self.last
    }
}

pub fn solve_a(input_file_path: &str) -> u32 {
    fs::read_to_string(input_file_path)
        .unwrap()
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| match c.to_digit(10) {
                    Some(n) => n,
                    None => 0,
                })
                .collect::<Vec<u32>>()
        })
        .map(|v| {
            v.iter().fold(Pair { first: 0, last: 0 }, |acc, n| match n {
                0 => acc,
                _ => match acc.first {
                    0 => Pair {
                        first: *n,
                        last: *n,
                    },
                    _ => Pair {
                        first: acc.first,
                        last: *n,
                    },
                },
            })
        })
        .map(|f| f.result())
        .sum::<u32>()
}

pub fn solve_b(input_file_path: &str) -> u32 {
    fs::read_to_string(input_file_path)
        .unwrap()
        .lines()
        .map(|line| {
            Regex::new(r"(oneight|twone|threeight|fiveight|sevenine|eightwo|eighthree|nineight|one|two|three|four|five|six|seven|eight|nine|\d)")
                .unwrap()
                .find_iter(line)
                .flat_map(|m| match m.as_str() {
                    "one" => vec![1],
                    "two" => vec![2],
                    "three" => vec![3],
                    "four" => vec![4],
                    "five" => vec![5],
                    "six" => vec![6],
                    "seven" => vec![7],
                    "eight" => vec![8],
                    "nine" => vec![9],

                    "oneight" => vec![1, 8],

                    "twone" => vec![2, 1],

                    "threeight" => vec![3, 8],

                    "fiveight" => vec![5, 8],

                    "sevenine" => vec![7, 9],

                    "eightwo" => vec![8, 2],
                    "eighthree" => vec![8, 3],

                    "nineight" => vec![9, 8],
                    other => vec![other.parse::<u32>().unwrap_or(0)],
                })
                .collect::<Vec<u32>>()
        })
        .map(|v|
            v.iter().fold(Pair { first: 0, last: 0 }, |acc, n| match n {
                0 => acc,
                _ => match acc.first {
                    0 => Pair {
                        first: *n,
                        last: *n,
                    },
                    _ => Pair {
                        first: acc.first,
                        last: *n,
                    },
                },
            })
        )
        .map(|f| f.result())
        .sum::<u32>()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve_a() {
        assert_eq!(solve_a(".\\src\\test_input\\day1a.txt"), 142);
    }

    #[test]
    fn test_solve_b() {
        assert_eq!(solve_b(".\\src\\test_input\\day1b.txt"), 281);
    }
}