function findPolicyAccountNumber(data, lineOfBusiness) {
    // Assuming data is already a JavaScript object (not a JSON string)
    if (data.pro && Array.isArray(data.pro)) {
        const product = data.pro.find(p => p.lob === lob);
        if (product) {
            console.log(`Policy Account Number: ${product.pan}`);
        } else {
            console.log("No matching lob found.");
        }
    } else {
        console.log("No pro available.");
    }
}


// Assuming you want to find the pan for a specific lob
const lineOfBusinessToFind = "yValue";
findPolicyAccountNumber(jsonData, lineOfBusinessToFind);
