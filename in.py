import matplotlib.pyplot as plt
import numpy as np

# Definimos los colores

colors = {
    "rosado_oscuro": (190/255, 84/255, 101/255),
    "negro": (11/255, 6/255, 6/255),
    "verde": (120/255, 165/255, 72/255),
    "azul": (84/255, 201/255, 184/255),
    "amarillo": (236/255, 221/255, 211/255)
}

# Creamos la figura y los ejes
fig, ax = plt.subplots()

# Dibujamos la mariposa usando parches
from matplotlib.patches import Ellipse

# Cuerpo de la mariposa
body = Ellipse((0.5, 0.5), width=0.1, height=0.4, angle=0, color=colors["negro"])
ax.add_patch(body)

# Alas superiores
wing1 = Ellipse((0.35, 0.65), width=0.3, height=0.5, angle=30, color=colors["rosado_oscuro"])
wing2 = Ellipse((0.65, 0.65), width=0.3, height=0.5, angle=-30, color=colors["rosado_oscuro"])
ax.add_patch(wing1)
ax.add_patch(wing2)

# Alas inferiores
wing3 = Ellipse((0.35, 0.35), width=0.3, height=0.4, angle=-30, color=colors["rosado_oscuro"])
wing4 = Ellipse((0.65, 0.35), width=0.3, height=0.4, angle=30, color=colors["rosado_oscuro"])
ax.add_patch(wing3)
ax.add_patch(wing4)

# Detalles en las alas (puntos)
detail1 = Ellipse((0.35, 0.65), width=0.1, height=0.15, angle=30, color=colors["verde"])
detail2 = Ellipse((0.65, 0.65), width=0.1, height=0.15, angle=-30, color=colors["verde"])
detail3 = Ellipse((0.35, 0.35), width=0.1, height=0.15, angle=-30, color=colors["azul"])
detail4 = Ellipse((0.65, 0.35), width=0.1, height=0.15, angle=30, color=colors["azul"])

ax.add_patch(detail1)
ax.add_patch(detail2)
ax.add_patch(detail3)
ax.add_patch(detail4)

# Configuramos el gráfico
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Guardamos la imagen
fig.savefig("C:/xampp0/htdocs", dpi=300, bbox_inches='tight')
plt.show()
