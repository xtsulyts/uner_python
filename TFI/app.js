document.addEventListener("DOMContentLoaded", function () {
    // Se seleccionan los elementos de entrada para cada tipo de búsqueda
    const buscadorVinosId = document.getElementById('buscador-vinos-id');
    const buscadorBodegasId = document.getElementById('buscador-bodegas-id');
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

        // Actualizamos el DOM con las tarjetas correspondientes
        if (tipo === 'vino') {
            listaVinos.innerHTML = listaHTML;
        } else if (tipo === 'bodega') {
            listaBodegas.innerHTML = listaHTML;
        } else if (tipo === 'cepa') {
            listaCepas.innerHTML = listaHTML;
        }
    }

    // Función para cargar los datos de un tipo específico (vinos, bodegas, cepas)
    function cargarDatos(tipo) {
        let url = '';
        if (tipo === 'vino') {
            //buscadorVinosId.innerHTML = listaHTML;
            url = 'http://127.0.0.1:5000/api/vinos';  // URL para obtener todos los vinos
        } else if (tipo === 'bodega') {
            url = 'http://127.0.0.1:5000/api/bodegas';  // URL para obtener todas las bodegas
        } else if (tipo === 'cepa') {
            url = 'http://127.0.0.1:5000/api/cepas';  // URL para obtener todas las cepas
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

    // Función para filtrar resultados: ahora maneja tanto búsqueda por nombre como por ID
    function filtrarResultados(query, tipo) {
        console.log(`Buscando con query: ${query}`);  // Agregado para depuración
        // Si el query parece un número (es un ID), realizamos una búsqueda por ID
        if (query && !isNaN(query)) {
            console.log(`Buscando por ID: ${query}`);  // Agregado para depuración
            const url = `http://127.0.0.1:5000/api/${tipo}/${query}`; // URL específica para buscar por ID

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(`Resultado por ID:`, data);  // Ver resultado por ID
                    // Si la búsqueda por ID devuelve datos, mostrar solo esa tarjeta
                    mostrarTarjetas([data], tipo);  // Envolvemos el resultado en un array
                })
                .catch(error => {
                    console.error('Error al buscar por ID:', error);
                });

        } else {
            // Si el query no es un número, buscamos por nombre
            fetch(`http://127.0.0.1:5000/api/${tipo}/${query}`)
                .then(response => response.json())
                .then(data => {
                    let resultados = data;

                    if (query) {
                        // Filtrar por nombre en lugar de ID
                        resultados = resultados.filter(item =>
                            item.nombre.toLowerCase().includes(query.toLowerCase())
                        );
                    }

                    mostrarTarjetas(resultados, tipo);
                })
                .catch(error => {
                    console.error('Error al filtrar los resultados:', error);
                });
        }
    }

    // Cargar los datos inicialmente
    cargarDatos('vino');
    cargarDatos('bodega');
    cargarDatos('cepa');

    // Añadir eventos de búsqueda para cada campo de ID
    buscadorVinosId.addEventListener('input', (event) => {
        console.log(`Input en vino: ${event.target.value}`);  // Agregado para depuración
        filtrarResultados(event.target.value, 'vino');
    });

    buscadorBodegasId.addEventListener('input', (event) => {
        console.log(`Input en bodega: ${event.target.value}`);  // Agregado para depuración
        filtrarResultados(event.target.value, 'bodega');
    });

    buscadorCepasId.addEventListener('input', (event) => {
        console.log(`Input en cepa: ${event.target.value}`);  // Agregado para depuración
        filtrarResultados(event.target.value, 'cepa');
    });
});
