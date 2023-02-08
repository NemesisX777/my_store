const ExampleComponent = () => {
    const [selectedValue, setSelectedValue] = React.useState("");
    const [data, setData] = React.useState([]);
    const [options, setOptions] = React.useState([]);

    const fetchData = async () => {
        const response = await fetch(`http://127.0.0.1:8000/api/categories/`);
        const json = await response.json();
        setOptions(json);
    };

    const fetchTableData = async (value = 8) => {
        const response = await fetch(`http://127.0.0.1:8000/api/categories/${value}/products/`);
        const json = await response.json();
        setData(json);
    };

    React.useEffect(() => {
        fetchData();
    }, []);

    React.useEffect(() => {
        if (selectedValue) {
            fetchTableData(selectedValue);
        }
    }, [selectedValue]);

    return (<div>
        <h3>Таблица на React.js</h3>
        <select onChange={(e) => setSelectedValue(e.target.value)}>
            <option value="">Select an option</option>
            {options.map((option) => (<option key={option.id} value={option.id}>
                {option.name}
            </option>))}
        </select>
        <table className="table table-bordered table-striped">
            <thead className="table-dark">
            <tr>
                <th scope="col">Номер</th>
                <th scope="col">Наименование</th>
                <th scope="col">Цена</th>
            </tr>
            </thead>
            <tbody className="table-group-divider">
            {data.map((row) => (
                <tr key={row.id}>
                    <th scope="row">{row.id}</th>
                    <td>{row.name}</td>
                    <td>{row.price}</td>
                </tr>
            ))}
            </tbody>
        </table>
    </div>);
};

ReactDOM.render(<ExampleComponent/>, document.getElementById("root"));
