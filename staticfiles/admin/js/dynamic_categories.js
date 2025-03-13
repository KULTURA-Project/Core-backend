// static/admin/js/dynamic_categories.js
document.addEventListener('DOMContentLoaded', function() {
    const categoryField = document.getElementById('id_category');
    
    categoryField.addEventListener('change', function() {
        const categoryId = this.value;
        const subcategoryField = document.getElementById('id_subcategory');
        
        // Use AJAX to fetch subcategories based on the selected category
        fetch('/admin/get_subcategories/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ categoryId: categoryId })
        })
        .then(response => response.json())
        .then(data => {
            // Clear existing options
            subcategoryField.innerHTML = '';
            
            // Add new options
            data.forEach(subcategory => {
                const option = document.createElement('option');
                option.value = subcategory.id;
                option.text = subcategory.name;
                subcategoryField.appendChild(option);
            });
        });
    });
});

// Helper function to get CSRF token
function getCookie(name) {
    let cookie = {};
    document.cookie.split(';').forEach(function(el) {
        let [key,value] = el.split('=');
        cookie[key.trim()] = value;
    })
    return cookie[name];
}
