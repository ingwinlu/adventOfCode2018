use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

type Result<T> = ::std::result::Result<T, Box<::std::error::Error>>;

fn main() -> Result<()> {
    let file = File::open("input")?;
    let f = BufReader::new(file);

    let mut ints = Vec::new();

    for line in f.lines() {
        let i = line?.parse::<i32>()?;
        ints.push(i);
    }


    let mut freq = HashSet::new();
    let mut temp = 0;

    for i in ints.iter().cycle() {
        if freq.contains(&temp) {
            println!("{}", temp);
            break
        }
        freq.insert(temp);
        temp += i;
    }
    Ok(())
}
