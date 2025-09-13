// Example JavaScript code to demonstrate Sourcery refactoring capabilities
// This file contains patterns that Sourcery would optimize

function processArray(items) {
    // Inefficient: manual loop instead of filter + map
    const result = [];
    for (let i = 0; i < items.length; i++) {
        if (items[i] > 0) {
            result.push(items[i] * 2);
        }
    }
    return result;
}

function findUser(users, id) {
    // Inefficient: manual loop instead of find()
    for (let i = 0; i < users.length; i++) {
        if (users[i].id === id) {
            return users[i];
        }
    }
    return null;
}

function checkPermissions(user) {
    // Inefficient: nested conditionals
    if (user !== null) {
        if (user.active === true) {
            if (user.role === 'admin') {
                return true;
            }
        }
    }
    return false;
}

function buildUrl(base, params) {
    // Inefficient: manual string concatenation
    let url = base;
    let first = true;
    for (const key in params) {
        if (first) {
            url = url + "?";
            first = false;
        } else {
            url = url + "&";
        }
        url = url + key + "=" + params[key];
    }
    return url;
}

// Example usage
const sampleData = [1, -2, 3, -4, 5];
console.log("Original:", sampleData);
console.log("Processed:", processArray(sampleData));

const users = [
    { id: 1, name: "Alice", active: true, role: "user" },
    { id: 2, name: "Bob", active: true, role: "admin" }
];

console.log("Found user:", findUser(users, 2));
console.log("Has permissions:", checkPermissions(users[1]));
console.log("URL:", buildUrl("https://api.example.com", { q: "search", limit: 10 }));