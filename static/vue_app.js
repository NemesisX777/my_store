var ExampleComponent = new Vue({
    el: "#VueProductTable",
    data: {
        selectedValue: "",
        data: [],
        options: []
    },
    methods: {
        fetchData: function () {
            axios.get("http://127.0.0.1:8000/api/categories/")
                .then(response => {
                    this.options = response.data;
                });
        },
        fetchTableData: function (value = 8) {
            axios.get(`http://127.0.0.1:8000/api/categories/${value}/products/`)
                .then(response => {
                    this.data = response.data;
                });
        }
    },
    created: function () {
        this.fetchData();
    },
    watch: {
        selectedValue: function (value) {
            if (value) {
                this.fetchTableData(value);
            }
        }
    }
});
