



fn main() {
    
    println!("----------------------");
    println!("----ARCHIVO BASICO----");
    println!("----------------------");
    
    
    
    let bo1: bool = false;
    let bol21: bool = !bo1;
    let cad1: String = "imprimir".to_string();
    let cad21: String = "cadena valida".to_string();
    let letra1: char = 'c';
    
    
    let val11 = 7 - (5 + 10 * (2 + 4 * (5 + 2 * 3)) - 8 * 3 * 3) + 50 * (6 * 2);
    let val21 = (2 * 2 * 2 * 2) - 9 - (8 - 6 + (3 * 3 - 6 * 5 - 7 - (9 + 7 * 7 * 7) + 10) - 5) + 8 - (6 - 5 * (2 * 3));
    let val31 = val11 + ((2 + val21 * 3) + 1 - ((2 * 2 * 2) - 2) * 2) - 2;
    
    println!("El valor de val11 es:              {}",val11);
    println!("El valor de val21 es:              {}",val21);
    println!("El valor de val31 es:              {}",val31);
    println!("El resultado de la operación es:  {}",val31);
    println!("El valor de bo1 es:                {}",bo1);
    println!("El valor de cad1 es:               {}",cad1);
    println!("El valor de cad21 es:               {}",cad21);
    println!("El valor de letra1 es:             {}",letra1);
    println!("El valor de bol21:            {}",bol21);
    println!("");
    

    
    let a:i64 = 100;
    let b:i64 = 100;
    let c:i64 = 7;
    let f:bool = true;
    let j:f64 = 10.0;
    let k:f64 = 10.0;
    
    println!("");
    println!("");
    if a > b || b < c {
        
        println!(">>>>>> Esto no debería de imprimirse");
    }else{
        let shionsa= 20;
        println!(">>>>>> Esto debería de imprimirse");
    }
    
    
    if a == b && j == k || 14 != c {
        println!(">>>>>> Esto debería de imprimirse");
    }else{
        println!(">>>>>> Esto no debería de imprimirse");
    }
    
    let val1:i64 = 5;
    let resp:i64 = 5;
    let mut valorVerdadero : i64 = 100;
    
    if((valorVerdadero == (50 + 50 + (val1 - val1))) && ! ! ! ! ! ! ! ! ! ! true) {
        println!(">>>>>> En este lugar deberia de entrar :)");
        valorVerdadero = 50;
    }
    else if (f || (valorVerdadero > 50)) && ((resp != 100) && ! ! ! ! ! f){
        println!(">>>>>> Aca no deberia de entrar :ccc");
        valorVerdadero = 70;
    }
    else{
        println!(">>>>>> Aca no deberia de entrar :cccc");
    }

    let x1: i64 = 15;

    if x1 % 2 == 0 {
        println!(">>>>> numeroPar ingreso a if verdadero, {} es par",x1);
    }
    else {
        println!(">>>>> numeroPar ingreso a if falso, {} no es par",x1);
    }



    let abs1:i64 = 7-11;
    let abs2:f64 = 10.0;
    let raiz1:i64 = 9;
    let raiz2:f64 = 100.0;
    
    
    println!("");
    println!("*************PRUEBA DE NATIVAS");
    println!(" valor de b: {:?}",b);
    
    println!(" valor absoluto1: {}",abs1.abs());
    println!(" valor absoluto2: {}",abs2.abs());
    println!(" valor raiz1: {}",(raiz1 as f64).sqrt());
    println!(" valor raiz2: {}",raiz2.sqrt());
    
    cont=0;
    loop {
        println!("Itera por siempre!");
        if cont==2{
            
            println!("Itera {}",cont);
            break;
        }
        cont=cont+1;
    }
    
    vari= loop {
        cont = cont + 1;
        if cont == 10 {
        break cont * 2;
        }
    };

    println!("El resultado es {}", vari);

    let n = 10;
    let operacion =
    if n < 10 {
    10 * n // Esta expresión devuelve un 'i64'
    } else if n == 10 {
    3 * n // Esta expresión devuelve un 'i64'
    } else {
    n / 2 // Esta expresión debe devolver un 'i64' también
    }; // <- ¡No olvides poner un punto y coma aquí!

    println!("{}", operacion);

    let arr= [[7,8,9],4,5,6];
    if arr.contains(&5) {
        println!("{}", arr.contains(&[7,8,9]) );
    }


    let numCadena = match 3 {
        1 => "uno",
        2 => "dos",
        3 => "tres",
        4 => "cuatro",
        _ => "cinco",
    };

    println!("Resultado match {}", numCadena);
}
