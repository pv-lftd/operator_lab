// Fill in the blanks
const file = [
  { id: 1, name: "Alice", role: "Admin" },
  { id: 2, name: "Bob", role: "User" },
  { id: 3, name: "Charlie", role: "Guest" }
];
// 1. Manually extract headers from the first object
const headers = Object.keys(file[0]); // type of the file
let js_result = "";
// 2. Build the header row manually
for (let i = 0; i < headers.length; i++) { // what loop
  js_result = js_result + headers[i];
  if (i < headers.length - 1) {
    js_result += ","; // Add comma between headers, but not at the end
  }
}
js_result += "\n"; // Move to the next line
// 3. Loop through each row (object) in the data array
for (let i = 0; i < file.length; i++) { // what loop?
  const row = file[i];
  // Loop through each header to get the values for this row
  for (let j = 0; j < headers.length; j++) { // should we add ++ or --
    const key = headers[j];
    js_result = js_result + row[key];
    if (j < headers.length - 1) {
      js_result += ","; // Add comma between values
    }
  }
  // Add a new line after each row except the very last one
  if (i < file.length - 1) { // whose length
    js_result = js_result + "\n"; // append to what
  }
}
console.log(js_result);
// Save manually into:
// javascript_output.csv
