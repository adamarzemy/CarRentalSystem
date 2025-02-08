// Function to convert text to number and round to 2 decimal places
export function textToNumber(text: string): number {
    const num = parseFloat(text);
    return isNaN(num) ? 0 : num;  // Return 0 if not a valid number
  }
  
// Function to convert text to number, round to 2 decimal places
export function textToTwoDecimalPlaces(text: string): number {
    const num = parseFloat(text);
    return isNaN(num) ? 0 : Math.round(num * 100) / 100; // Round to 2 decimal places
}
  