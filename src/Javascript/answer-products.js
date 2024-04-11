function findPolicyAccountNumbers(data, linesOfBusiness) {
    let results = {};

    // Ensure there are products to search through
    if (data.products && Array.isArray(data.products)) {
        linesOfBusiness.forEach(lineOfBusiness => {
            const product = data.products.find(p => p.lineOfBusiness === lineOfBusiness);
            if (product) {
                // Store the policyAccountNumber associated with the lineOfBusiness
                results[lineOfBusiness] = product.policyAccountNumber;
            } else {
                // Indicate no match was found for this lineOfBusiness
                results[lineOfBusiness] = "No matching lineOfBusiness found.";
            }
        });
    } else {
        console.log("No products available.");
        return;
    }

    return results;
}


const linesOfBusinessToFind = ["xValue", "yValue", "zValue"]; // Include a non-existent value for demonstration
const results = findPolicyAccountNumbers(jsonData, linesOfBusinessToFind);

console.log(results);
