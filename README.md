# Pantry Pal

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge">
  <img alt="Contributions Welcome" src="https://img.shields.io/badge/contributions-welcome-brightgreen?style=for-the-badge">
  <img alt="Maintained" src="https://img.shields.io/badge/maintained-yes-purple?style=for-the-badge">
</p>

A smart pantry manager to track your inventory, discover recipes based on what you have, and build shopping lists—entirely offline, no backend or database required.

| **View Live Demo** | **Report a Bug** | **Request a Feature** |
| :---: | :---: | :---: |
| [**`Try it Now →`**](https://tabitha-dev.github.io/Pantry_Pal/) | [**`Submit an Issue`**](https://github.com/tabitha-dev/Pantry_Pal/issues) | [**`Suggest an Idea`**](https://github.com/tabitha-dev/Pantry_Pal/issues) |

---

## Why Use Pantry Pal?

Pantry Pal gives you instant visibility into what’s in your pantry, fridge, and freezer. It helps you find recipes based on what you have and auto-generates shopping lists for missing ingredients. All your data lives directly in your browser’s IndexedDB, ensuring complete privacy and offline access.

## Key Features

* 🗂️ **Inventory Management**: Add, update, or delete items in Pantry, Fridge & Freezer.  
* 🔍 **Search & Filter**: Live-filter your inventory by name or category.  
* 🍽️ **Recipe Suggestions**: Fetch recipes & calculate a “match score” against your stock.  
* 🛒 **Smart Shopping List**: One-click to add missing ingredients to your list.  
* 📈 **Analytics Dashboard**: Modern charts to visualize inventory breakdown by category.  
* 💾 **Local Persistence**: Data stored in IndexedDB—completely offline & private.  

---

## Tech Stack & Tools

This application is built entirely with modern, client-side technologies, making it lightweight, fast, and easy to run anywhere.

| Technology                   | Purpose                                |
| :--------------------------- | :------------------------------------- |
| **React (UMD + Babel)**      | UI rendering without a build step      |
| **Tailwind CSS**             | Utility-first styling                  |
| **Chart.js**                 | Interactive data visualizations        |
| **chartjs-plugin-datalabels**| In-chart data labels                   |
| **idb**                      | Simplified IndexedDB interactions      |
| **ThemealDB API**            | Recipe data source                     |
| **Babel Standalone**         | In-browser JSX compilation             |

---

## Getting Started

This application is a single HTML/JS page and is incredibly simple to use.

1.  **Clone the repo**:  
    ```bash
    git clone https://github.com/tabitha-dev/Pantry_Pal.git
    cd Pantry_Pal
    ```
2.  **Serve locally**:  
    ```bash
    # Python 3 HTTP server
    python3 -m http.server 8000
    ```
3.  **Open in Browser**:  
    ```txt
    http://localhost:8000/
    ```

### A Note on Data Persistence

Your pantry data is stored in your browser’s IndexedDB. Clearing your site data or browser cache will permanently erase it—be sure to back up any critical information.

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply [open an issue](https://github.com/tabitha-dev/Pantry_Pal/issues) with the tag “enhancement”.

## License

Distributed under the MIT License. See `LICENSE` for more information.  
