let imagestring = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA8AAAAIcCAYAAAA5Xcd7AAAAAXNSR0IArs4c6QAAIABJREFUeF7snQecXFXZ/5/tyW4aNSiBgPQiGFDpxYaoQJCOdJXQEZQaXhGkiNKlSgALgoB0fAER6SAikJcW6VJCE1K3JVv//9+ZOZO7d+6de2d3djOb+Z7PB5Hsqd9zCPndp1WZWa/"

let cleanstring = imagestring.split(",")[1]
let byteCharacter = atob(cleanstring)
console.log("CLEAN:", cleanstring)
const byteNumbers = new Array(byteCharacter.length)



for (let i = 0; i < byteCharacter.length; i++){
    byteNumbers[i] = byteCharacter.charCodeAt(i)
} // now byteNumbers has the numbers of the base64
console.log("ByteNumbers", byteNumbers)
const byteArray = new Uint8Array(byteNumbers)

const decoded = btoa(byteNumbers)
console.log("DECODEDBYTEARRAY", decoded)
const blobImage = new Blob([byteArray], {type: "image/png"});
