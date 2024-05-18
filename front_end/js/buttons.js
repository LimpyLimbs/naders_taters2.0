const incrementButtons = document.querySelectorAll('.increment');
const decrementButtons = document.querySelectorAll('.decrement');
const addToCartButtons = document.querySelectorAll('.add-to-cart');

const itemCounts = {
    classic: 0,
    barbeque: 0,
    cheddar: 0,
    dill_pickle: 0,
    jalapano: 0,
    kettle_cooked: 0,
    salt_and_vinegar: 0,
    salt_and_pepper: 0,
    sour_cream_and_onion: 0
};

const cart = {};

function updateItemCount(id) {
    const itemCountSpan = document.getElementById(`item_count_${id}`);
    itemCountSpan.textContent = itemCounts[id];
}

function updateCartDisplay() {
    // Logic to update the cart display goes here (e.g., updating the DOM, showing a modal, etc.)
    console.log('Cart:', cart);
}

incrementButtons.forEach(button => {
    button.addEventListener('click', function() {
        const id = button.getAttribute('data-id');
        itemCounts[id]++;
        updateItemCount(id);
    });
});

decrementButtons.forEach(button => {
    button.addEventListener('click', function() {
        const id = button.getAttribute('data-id');
        if (itemCounts[id] > 0) {
            itemCounts[id]--;
            updateItemCount(id);
        }
    });
});

addToCartButtons.forEach(button => {
    button.addEventListener('click', function() {
        const id = button.getAttribute('data-id');
        if (itemCounts[id] > 0) {
            if (cart[id]) {
                cart[id] += itemCounts[id];
            } else {
                cart[id] = itemCounts[id];
            }
            itemCounts[id] = 0; // Reset item count after adding to cart
            updateItemCount(id);
            updateCartDisplay();
        }
    });
});
