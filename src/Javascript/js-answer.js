// Assuming the JSON data is stored in a variable named jsonString
const jsonString =

// Parse the JSON string into an object
const data = JSON.parse(jsonString);

// Function to extract mobile contacts that are deliverable
function extractDeliverableMobileContacts(data) {
    // Check if contacts exist and filter based on conditions
    if (data.contacts && Array.isArray(data.contacts)) {
        return data.contacts.filter(contact =>
            contact.contactType === "Mobile" && contact.deliverable === true
        ).map(contact => contact.contact);
    }
    return [];
}

// Extract the contacts and log them
const mobileContacts = extractDeliverableMobileContacts(data);
console.log(mobileContacts); // Output: ['602334331']
