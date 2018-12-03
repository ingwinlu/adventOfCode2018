use std::fs::File;
use std::io::{BufRead, BufReader, Result};

fn main() -> Result<()> {
    let file = File::open("input")?;
    let f = BufReader::new(file);
    let mut temp = 0;
    for line in f.lines() {
        let my_int = line?.parse::<i32>().unwrap();
        temp += my_int;
    }

    println!("{}", temp);
    Ok(())
}
