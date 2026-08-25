const scores = [85, 87, 90, 94, 88];

// Calculate average
let total = 0;
for (const score of scores) {
  total += score;
}
const avg = total / scores.length;

// Conditional Logic (if-else)
let result;
if (avg > 95) {
  result = "Meeting Expectations";
} else {
  result = "Needs Improvement";
}

console.log(`Average: ${avg} - ${result}`);
