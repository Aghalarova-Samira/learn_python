function ebob(a , b){
    let  c= null
    if( a <b){
        c= a
    }else if(b<a){
        c = b
    }

   for (let i = c; i >0; i--) {
      if( a % i == 0 && b % i == 0 ){
          console.log(i)
          return

      }
       
   }


}


ebob(50 , 70)