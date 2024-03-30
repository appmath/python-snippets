const jsonString

const data = JSON.parse(jsonString);

function findDeliverableMobileContact(data) {
    if (data.contacts && Array.isArray(data.contacts)) {
        const mobileContact = data.contacts.find(contact =>
            contact.contactType === "Mobile" && contact.deliverable === true
        );
        return mobileContact ? mobileContact.contact : null;
    }
    return null;
}

const mobileContact = findDeliverableMobileContact(data);
console.log(mobileContact); // Output: "602334331"
