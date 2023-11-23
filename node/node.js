let patient = "john players"
let age = 20
let new_patient = {patient,age}

console.log(new_patient);
console.log("the type of age is ==> ", typeof age);

console.log('We can even use double "quotes" in string');


const nArray = ["1","2","3","4","text"]

if("text".includes("ten")){
    console.log("yes it is present");
}else{
    console.log("no it is not present");
}

if(nArray.includes("1")){
    console.log("yes this one is there");
}else{
    console.log("no this one is not there");
}

const dRray = [{x:"1",z:"3"},{y:"2"}]

console.log(dRray[0].z);

// ----------------------------------------
// replace array elements
const org_array = [1,7,3,4,5]

org_array[1] = 2

console.log(org_array)