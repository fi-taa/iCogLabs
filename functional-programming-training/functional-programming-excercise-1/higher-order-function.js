function debounce(func, delay) {
    let timeout;

    return function(...args) {
        clearTimeout(timeout);

        timeout = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}

function fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    console.log(n)
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(debounce(fibonacci(10),2))