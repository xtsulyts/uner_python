document.addEventListener("DOMContentLoaded", function () {
    const buscador = document.getElementById('buscador');
    const resultados = document.getElementById('resultados');

    // Esta función hará la búsqueda por ID o nombre dependiendo de lo que se ingrese
    function buscarDatos(query) {
        let url = '';
        
        // Si el query parece un ID (puede ser un UUID o un número)
        if (esIdValido(query)) {
            console.log(`Buscando por ID: ${query}`);
            url = `http://localhost:5000/api/vinos/${query}`; // URL para búsqueda por ID de vino
        } else {
            console.log(`Buscando por nombre: ${query}`);
            url = `http://localhost:5000/api/vinos`; // URL para búsqueda por nombre
        }

        console.log(`URL de solicitud: ${url}`);  // Verifica la URL generada para la solicitud

        fetch(url)
            .then(response => {
                console.log('Respuesta recibida:', response); // Ver respuesta del backend
                if (!response.ok) {
                    throw new Error(`Error en la respuesta: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Datos recibidos:', data);  // Ver los datos obtenidos del backend
                // Limpiar resultados previos
                resultados.innerHTML = '';

                // Si buscamos por ID, mostramos un solo resultado
                if (esIdValido(query)) {
                    mostrarResultados([data]);
                } else {
                    // Si es por nombre, mostramos varios resultados
                    mostrarResultados(data);
                }
            })
            .catch(error => {
                console.error('Error al obtener los resultados:', error);
                resultados.innerHTML = '<p class="text-danger">Hubo un error al buscar los datos. Intenta nuevamente.</p>';
            });
    }

    // Función para verificar si el query parece un ID válido
    function esIdValido(query) {
        // Comprobar si el query es un UUID o un número
        return /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/.test(query) || !isNaN(query);
    }

    // Función para mostrar los resultados en la interfaz
    function mostrarResultados(datos) {
        if (datos.length === 0) {
            resultados.innerHTML = '<p class="text-info">No se encontraron resultados.</p>';
        }
        datos.forEach(item => {
            let tarjeta = `
                <div class="col-12 col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">${item.nombre}</h5>
                            <p class="card-text">ID: ${item.id}</p>
                            <p class="card-text">Bodega: ${item.bodega}</p>
                            <p class="card-text">Cepas: ${item.cepas.join(', ')}</p>
                            <p class="card-text">Partidas: ${item.partidas.join(', ')}</p>
                        </div>
                    </div>
                </div>
            `;
            resultados.innerHTML += tarjeta;
        });
    }

    // Event listener para el campo de búsqueda
    buscador.addEventListener('input', (event) => {
        const query = event.target.value.trim();
        if (query) {
            buscarDatos(query);
        } else {
            resultados.innerHTML = '';  // Limpiar resultados si el campo está vacío
        }
    });
});
