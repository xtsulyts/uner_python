document.addEventListener("DOMContentLoaded", function () {
    // Se seleccionan los elementos de entrada para cada tipo de búsqueda
    const buscadorVinosNombre = document.getElementById('buscador-vinos-nombre');
    const buscadorVinosId = document.getElementById('buscador-vinos-id');
    const buscadorBodegasNombre = document.getElementById('buscador-bodegas-nombre');
    const buscadorBodegasId = document.getElementById('buscador-bodegas-id');
    const buscadorCepasNombre = document.getElementById('buscador-cepas-nombre');
    const buscadorCepasId = document.getElementById('buscador-cepas-id');

    // Se seleccionan las secciones de las listas para vinos, bodegas y cepas
    const listaVinos = document.getElementById('lista-vinos');
    const listaBodegas = document.getElementById('lista-bodegas');
    const listaCepas = document.getElementById('lista-cepas');

    // Función para mostrar las tarjetas con los datos obtenidos
    function mostrarTarjetas(datos, tipo) {
        let listaHTML = '';
        datos.forEach(item => {
            let tarjeta = `
                <div class="col-12 col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">${item.nombre}</h5>
                            <p class="card-text">ID: ${item.id}</p>
            `;
            if (tipo === 'vino') {
                tarjeta += `
                    <p class="card-text">Bodega: ${item.bodega}</p>
                    <p class="card-text">Cepas: ${item.cepas.join(', ')}</p>
                    <p class="card-text">Partidas: ${item.partidas.join(', ')}</p>
                `;
            }
            tarjeta += `
                        </div>
                    </div>
                </div>
            `;
            listaHTML += tarjeta;
        });

        if (tipo === 'vino') {
            listaVinos.innerHTML = listaHTML;
        } else if (tipo === 'bodega') {
            listaBodegas.innerHTML = listaHTML;
        } else if (tipo === 'cepa') {
            listaCepas.innerHTML = listaHTML;
        }
    }

    function cargarDatos(tipo) {
        let url = '';
        if (tipo === 'vino') {
            url = 'http://127.0.0.1:5000/api/vinos';  // URL completa
        } else if (tipo === 'bodega') {
            url = 'http://127.0.0.1:5000/api/bodegas';  // URL completa
        } else if (tipo === 'cepa') {
            url = 'http://127.0.0.1:5000/api/cepas';  // URL completa    
        }
    
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Ver los datos en la consola
                mostrarTarjetas(data, tipo);
            })
            .catch(error => {
                console.error('Error al cargar los datos:', error);
            });
    }
    

    // Función para filtrar resultados
    function filtrarResultados(query, tipo) {
        fetch(`/api/${tipo}`)
            .then(response => response.json())
            .then(data => {
                let resultados = data;

                if (query) {
                    // Filtrar por nombre o por ID dependiendo del campo
                    resultados = resultados.filter(item =>
                        item.nombre.toLowerCase().includes(query.toLowerCase()) || 
                        item.id.toString().includes(query)
                    );
                }

                mostrarTarjetas(resultados, tipo);
            })
            .catch(error => {
                console.error('Error al filtrar los resultados:', error);
            });
    }

    // Cargar los datos inicialmente
    cargarDatos('vino');
    cargarDatos('bodega');
    cargarDatos('cepa');

    // Añadir eventos de búsqueda
    buscadorVinosNombre.addEventListener('input', (event) => filtrarResultados(event.target.value, 'vino'));
    buscadorVinosId.addEventListener('input', (event) => filtrarResultados(event.target.value, 'vino'));
    buscadorBodegasNombre.addEventListener('input', (event) => filtrarResultados(event.target.value, 'bodega'));
    buscadorBodegasId.addEventListener('input', (event) => filtrarResultados(event.target.value, 'bodega'));
    buscadorCepasNombre.addEventListener('input', (event) => filtrarResultados(event.target.value, 'cepa'));
    buscadorCepasId.addEventListener('input', (event) => filtrarResultados(event.target.value, 'cepa'));
});
