const contacts

function findDeliverableContacts(contacts) {
    let result = {
        email: null,
        mobile: null
    };

    // Find Email
    const emailContact = contacts.find(contact =>
        contact.contactType === "Email" && contact.deliverable === true
    );
    if (emailContact) {
        result.email = emailContact.contact;
    }

    // Find Mobile
    const mobileContact = contacts.find(contact =>
        contact.contactType === "Mobile" && contact.deliverable === true
    );
    if (mobileContact) {
        result.mobile = mobileContact.contact;
    }

    return result;
}

const {email, mobile} = findDeliverableContacts(contacts);
console.log(`Email: ${email}, Mobile: ${mobile}`);
// Output: Email: someEmail@example.com, Mobile: 602334331
