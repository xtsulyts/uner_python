import pyfiglet
from rich.console import Console
from rich.text import Text

# Configuración de la consola
console = Console()
console.print("")
console.print("")
# Arte ASCII para el título principal
ascii_art = pyfiglet.figlet_format("Walter Frias")
console.print(f"[bold rgb(0,255,0)]{ascii_art}[rgb(0,255,0)]")

# Subtítulo
ascii_art_styled = pyfiglet.figlet_format("Web3 Developer", font="slant")
console.print(f"[bold rgb(0,255,0)]{ascii_art_styled}[/bold rgb(0,255,0)]")
console.print("")
# Clase del CV
class Web3Developer:
    def __init__(self):
        self.name = "Walter Frias"
        self.contact = {
            "Email": "531xtsulyts@gmail.com",
            "GitHub": "https://github.com/xtsulyts",
            "LinkedIn": "https://www.linkedin.com/in/walter-manuel-frias-61b03244/"
        }
        self.education = [
            {
                "title": "Técnico Universitario en Desarrollo Web (30% completado, Promedio: 8)",
                "institution": "Universidad Nacional de Entre Ríos, Argentina",
                "year": "2024 (en curso)"
            },
            {
                "title": "Profesor Nacional de Artes Visuales",
                "institution": "ESEA Manuel Belgrano, Buenos Aires",
                "year": "2019 - 2024"
            },
            {
                "title": "Maestro Mayor de Obras",
                "institution": "Escuela Técnica República Argentina, Buenos Aires",
                "year": "1997 - 2001"
            }
        ]
        self.skills = {
            "languages": ["Python", "JavaScript", "TypeScript", "Solidity", "CSS", "HTML", "PostgreSQL"],
            "frameworks_libraries": ["Django", "Flask", "Vue.js", "React.js", "Hardhat"],
            "blockchain_technologies": ["Ethereum (EVM)", "IPFS", "ERC Standards"],
            "tools": ["Remix", "Node.js"]
        }
        self.projects = [
            {
                "name": "Despliegue de Contratos Inteligentes",
                "description":"Creación y prueba de contratos inteligentes como ERC20, Pool Swap y Subastas.",
                "technologies": ["Solidity", "Hardhat", "Remix", "TypeScript", "Node.js"],
                "networks": ["Sepolia", "Scroll Sepolia"]
            }
        ]
        self.certifications = [
            {
                "title": "Ethereum Developer",
                "institution": "ETH-KIPU",
                "year": 2024
            },
            {
                "title": "Python FullStack",
                "institution": "Codo a Codo, Buenos Aires",
                "year": 2023
            },
            {
                "title": "Django Especialización",
                "institution": "Codo a Codo, Buenos Aires",
                "year": 2023
            },
            {
                "title": "UX/UI",
                "institution": "Talento Tech, Buenos Aires",
                "year": 2024
            }
        ]
        self.languages = {
            "English": "Intermediate",
            "Spanish": "Native"
        }
        self.objective = """
        Apasionado por el desarrollo Web3, busco aportar mis habilidades
        en contratos inteligentes y dApps mientras sigo creciendo 
        profesionalmente. Con una sólida base autodidacta y proyectos prácticos, 
        estoy preparado para asumir desafíos en el sector.
        """

    def display(self):
        console.print(Text("🔗  Contacto:", style="bold rgb(0,255,0)"))
        console.print("")
        for k, v in self.contact.items():
            console.print(f"[bold rgb(255,0,255)]{k}:[/bold rgb(255,0,255)] {v}")

        
        console.print("\n[bold rgb(0,255,0)]🎓  Educación:[/bold rgb(0,255,0)]")

        for edu in self.education:
            console.print("")
            console.print(f"[bold rgb(0,0,255)]{edu['title']}[/bold rgb(0,0,255)] \n - {edu['institution']} ({edu['year']})")
            console.print("")
        
        console.print(Text("🛠️   Habilidades Técnicas:", style="bold rgb(0,255,0)"))

        
        console.print("")
        console.print(f"[bold rgb(255,0,255)]Lenguajes:[/bold rgb(255,0,255)] {', '.join(self.skills['languages'])}")
        console.print("")
        console.print(f"[bold rgb(255,0,255)]Frameworks/Librerías:[/bold rgb(255,0,255)] {', '.join(self.skills['frameworks_libraries'])}")
        console.print("")
        console.print(f"[bold rgb(255,0,255)]Blockchain:[/bold rgb(255,0,255)] {', '.join(self.skills['blockchain_technologies'])}")
        console.print("")
        console.print(f"[bold rgb(255,0,255)]Herramientas:[/bold rgb(255,0,255)] {', '.join(self.skills['tools'])}")
        console.print("")
        console.print(Text("📂  Proyectos Realizados:", style="bold rgb(0,255,0)"))
       

        for proj in self.projects:
            console.print("")
            console.print(f"[bold rgb(0,0,255)]{proj['name']}:[/bold rgb(0,0,255)]\n {proj['description']}")
            console.print("")
            console.print(f"[bold rgb(255,0,255)]Tecnologías:[/bold rgb(255,0,255)] {', '.join(proj['technologies'])}")
            console.print("")
            console.print(f"[bold rgb(255,0,255)]Redes:[/bold rgb(255,0,255)] {', '.join(proj['networks'])}\n")
        
        console.print(Text("📜  Certificaciones:", style="bold rgb(0,255,0)"))
        #console.print("\n[bold rgb(0,255,0]📜 Certificaciones:[/bold rgb(0,255,0]")

        for cert in self.certifications:
            console.print("")
            console.print(f"[bold cyan]{cert['title']}[/bold cyan] - {cert['institution']} ({cert['year']})")

        console.print("")
        console.print(Text("🌐  Idiomas:", style="bold rgb(0,255,0)"))
        
        for lang, lvl in self.languages.items():
            console.print("")
            console.print(f"[bold rgb(255,0,255)]{lang}:[/bold rgb(255,0,255)]{lvl}")
        
        console.print("\n[bold rgb(0,255,0)]🎯 Objetivo Profesional:[/bold rgb(0,255,0)]")
        console.print(self.objective)
        console.print("")
        console.print("")

if __name__ == "__main__":
    walter = Web3Developer()
    walter.display()