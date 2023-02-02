new Vue ({
    "el": '#products_app',
    "data": {
        "products": [],
        "categories": []
    },
    "created": function () {
        const vm_1 = this;
        axios.get('http://127.0.0.1:8000/api/products/')
            .then(function (response) {
                console.log(response.data)
                vm_1.products = response.data
            })
        const vm_2 = this;
        axios.get('http://127.0.0.1:8000/api/categories/')
            .then(function (response) {
                console.log(response.data)
                vm_2.categories = response.data
            })
    }
})
