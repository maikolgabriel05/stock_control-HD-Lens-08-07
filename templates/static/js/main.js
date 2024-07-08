const getSales = () => ({
    urlSale: 'http://localhost:8000/shopping/carts/',
    urlProduct: 'http://localhost:8000/api/products/',
    urlCustomer: 'http://localhost:8000/api/customers/',
    isLoading: false,
    sales: [],
    products: [],
    customers: [],
    itens: [],
    selectedCustomer: '',

    init() {
        this.getData();
    },

    getData() {
        this.isLoading = true;

        // Pega os dados das vendas.
        fetch(this.urlSale)
            .then(response => response.json())
            .then(data => {
                this.sales = data;
                console.log('Dados de venda obtidos:', this.sales); // Adiciona console.log()
                // Se não tiver produtos, adiciona um item vazio à lista de vendas
                if (this.sales.length === 0) {
                    this.sales = [{
                        'name': '',
                        'stock': null,
                        'price': null
                    }];
                }
            });

        // Pega os dados dos produtos.
        fetch(this.urlProduct)
            .then(response => response.json())
            .then(data => {
                this.products = data;
                console.log('Dados de produtos obtidos:', this.products); // Adiciona console.log()
            });

        // Pega os dados do cliente.
        fetch(this.urlCustomer)
            .then(response => response.json())
            .then(data => {
                this.customers = data;
                console.log('Dados do cliente obtidos:', this.customers); // Adiciona console.log()
                this.isLoading = false;
                // Se não tiver clientes, adiciona um item vazio à lista de clientes
                if (data.length === 0) {
                    this.customers = [{
                        pk: null,
                        name: ''
                    }];
                }
            });
    },

    addRow() {
        this.sales.push({
            'name': '',
            'stock': null,
            'price': null
        });
    },

    removeRow(index) {
        // Verifica se o índice é válido
        if (index >= 0 && index < this.sales.length) {
            // Remove a linha com o índice especificado
            this.sales.splice(index, 1);
        }
    },

    findProduct(product, index) {
        const item = this.products.find((item) => {
            return item.pk == parseInt(product);
        });
        if (item) this.sales[index].price = item.price;
    },

    async saveData() {
        if (!this.selectedCustomer) {
            console.error('O cliente deve ser selecionado.');
            return;
        }

        const items = this.sales.map(item => ({
            product: parseInt(item.product),
            stock: parseInt(item.stock),
            price: parseFloat(item.price),
        }));

        const payload = {
            customer: parseInt(this.selectedCustomer),
            itens: items
        };

        console.log('Enviando dados para o servidor:', payload);

        const response = await fetch('http://localhost:8000/shopping/carts/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        console.log('Resposta do servidor:', data);

        // Limpar a lista de vendas
        this.sales = [{
            'name': '',
            'stock': null,
            'price': null
        }];
    },


    total() {
        return this.sales.reduce((acc, sale) => {
            return acc + (sale.stock * sale.price);
        }, 0).toFixed(2);
    },
});

// Inicializa a função getSales
const app = getSales();
app.init();
