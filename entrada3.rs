fn main () {


  
  var= [[3,4],[5,6],7];
  var[1][1]=11;
  println!("{:?}", var[1]);
  
  let numero = 15;

  match numero {
  
    1 | 2 | 3 => {
    let x = 100;
    println!("Rango de 1 a 3");
    },
    6 | 7 | 8 => println!("Rango de 6 a 8");,
    "9" => println!("Rango de 6 a 8");,
    _ => println!("Resto de casos");,
  }


}
