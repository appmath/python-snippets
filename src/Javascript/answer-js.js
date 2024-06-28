if (Array.isArray(e.response.data.errors)) {
    const errors = e.response.data.errors;
    const errorExists = errors.some(error => error.title === SOME_NAME);

    if (errorExists) {
        // Handle the specific error case
    }
}