new Vue({
    el: "#products_app",
    data: {
        products: [],
        categories: [],
        selectedCategory: ""
    },
    created: function () {
        const vm = this;
        axios.get("http://127.0.0.1:8000/api/products/")
            .then(function (response) {
                vm.products = response.data;
            });
        axios.get("http://127.0.0.1:8000/api/categories/")
            .then(function (response) {
                vm.categories = response.data;
            });
    },
    methods: {
        fetchProductsByCategory: function () {
            const vm = this;
            axios.get("http://127.0.0.1:8000/api/categories/{vm.selectedCategory}/products/")
                .then(function (response) {
                    vm.products = response.data;
                });
        }
    }
});