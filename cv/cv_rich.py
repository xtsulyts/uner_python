from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

# Crear un objeto Console
console = Console()

# Títulos estilizados
console.print(Text("Walter Frias - Web3 Developer", style="bold cyan", justify="center"))
console.print(Text("Apasionado por el desarrollo Web3 y el aprendizaje continuo.", style="italic", justify="center"))
console.print("\n")

# Sección de contacto
console.print(Panel("[bold]Contacto[/bold]\n"
                    "- Email: [cyan]531xtsulyts@gmail.com[/cyan]\n"
                    "- GitHub: [cyan]https://github.com/xtsulyts[/cyan]\n"
                    "- LinkedIn: [cyan]https://www.linkedin.com/in/walter-manuel-frias-61b03244/[/cyan]", 
                    title="📬 Contacto", style="green"))

# Tabla de educación
edu_table = Table(title="🎓 Formación Académica", style="blue")
edu_table.add_column("Título", style="bold magenta")
edu_table.add_column("Institución", style="cyan")
edu_table.add_column("Año", style="yellow")
edu_table.add_row("Técnico en Desarrollo Web (30%, Promedio: 8)", 
                  "Universidad Nacional de Entre Ríos, Argentina", "2024 (en curso)")
edu_table.add_row("Profesor Nacional de Artes Visuales", 
                  "ESEA Manuel Belgrano, Buenos Aires", "2019 - 2024")
edu_table.add_row("Maestro Mayor de Obras", 
                  "Escuela Técnica República Argentina, Buenos Aires", "1997 - 2001")
console.print(edu_table)

# Tabla de habilidades
skills_table = Table(title="🛠️ Habilidades Técnicas", style="blue")
skills_table.add_column("Categoría", style="bold magenta")
skills_table.add_column("Detalles", style="cyan")
skills_table.add_row("Lenguajes", "Python, JavaScript, TypeScript, Solidity, CSS, HTML, PostgreSQL")
skills_table.add_row("Frameworks/Librerías", "Django, Flask, Vue.js, React.js, Hardhat")
skills_table.add_row("Blockchain", "Ethereum (EVM), IPFS, ERC Standards")
console.print(skills_table)

# Sección de proyectos
console.print(Panel("[bold]Proyectos Realizados[/bold]\n"
                    "- [bold]Despliegue de Contratos Inteligentes:[/bold] ERC20, Pool Swap, Subasta.\n"
                    "  - Tecnologías: Solidity, Hardhat, Remix, TypeScript, Node.js\n"
                    "  - Redes: Sepolia, Scroll Sepolia", 
                    title="🛠️ Proyectos", style="green"))

# Tabla de certificaciones
cert_table = Table(title="📜 Certificaciones", style="blue")
cert_table.add_column("Título", style="bold magenta")
cert_table.add_column("Institución", style="cyan")
cert_table.add_column("Año", style="yellow")
cert_table.add_row("Ethereum Developer", "ETH-KIPU", "2024")
cert_table.add_row("Python FullStack", "Codo a Codo, Buenos Aires", "2023")
cert_table.add_row("Django Especialización", "Codo a Codo, Buenos Aires", "2023")
cert_table.add_row("UX/UI", "Talento Tech, Buenos Aires", "2024")
console.print(cert_table)

# Sección de objetivo profesional
console.print(Panel("**Objetivo Profesional**\n"
                    "Apasionado por el desarrollo Web3, busco aportar mis habilidades en contratos inteligentes y dApps "
                    "mientras sigo creciendo profesionalmente. Con una sólida base autodidacta y proyectos prácticos, "
                    "estoy preparado para asumir desafíos en el sector.", 
                    title="🎯 Objetivo Profesional", style="green"))
