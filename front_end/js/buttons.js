const incrementButtons = document.querySelectorAll('.increment');
const decrementButtons = document.querySelectorAll('.decrement');

const itemCounts = {
    classic: 0,
    barbeque: 0, 
    cheddar: 0,
    'dill-pickle': 0,
    jalapano: 0,
    'kettle-cooked': 0,
    'salt-and-vinegar': 0,
    'salt-and-pepper': 0,
    'sour-cream-and-onion': 0
};

function updateItemCount(id) {
    const itemCountSpan = document.getElementById(`item-count-${id}`);
    itemCountSpan.textContent = itemCounts[id];
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
