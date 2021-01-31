// event listener to add items to cart from cart view
var updateBtns = document.getElementsByClassName("updatecart");

for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function(){
        var action2 = this.dataset.action
        var productId2 = this.dataset.product

//        console.log("Product Id: ", productId2, ", ", "action: ", action2);
        updateUserCart(productId2, action2);
    })
}


// event listener to add items to cart from detail view
document.getElementById("update").addEventListener("click", function(){
    var action = document.getElementById("update").getAttribute("data-action");
    var productId = document.getElementById("update").getAttribute("data-product");

//    console.log("Product Id: ", productId, ", ", "action: ", action);
    updateUserCart(productId, action);
})

// function to add to cart on details page
function updateUserCart(productId, action){
    console.log("sending data")

    var url = '/add_cart/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'x-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        location.reload()
    })

//    alert("item has been added");
}

