const incrementButton = document.querySelector('.increment');
const decrementButton = document.querySelector('.decrement');
const itemCountSpan = document.getElementById('item-count');

// Initial item count
let itemCount = 0;

// Update item count function
function updateItemCount() {
    itemCountSpan.textContent = itemCount;
}

// Event listener for increment button
incrementButton.addEventListener('click', function() {
    itemCount++;
    updateItemCount();
});

// Event listener for decrement button
decrementButton.addEventListener('click', function() {
    if (itemCount > 0) {
        itemCount--;
        updateItemCount();
    }
});