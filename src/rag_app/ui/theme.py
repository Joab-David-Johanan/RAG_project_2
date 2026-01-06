import streamlit.components.v1 as components


def inject_cursor_particles():
    components.html(
        """
        <style>
        html, body {
            margin: 0;
            padding: 0;
            background: transparent;
            overflow: hidden;
        }

        .spark {
            position: absolute;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: radial-gradient(circle, #8b5cf6, #6366f1, transparent);
            pointer-events: none;
            animation: fade 0.8s forwards;
        }

        @keyframes fade {
            to {
                opacity: 0;
                transform: scale(3);
            }
        }
        </style>

        <script>
        document.addEventListener("mousemove", (e) => {
            const spark = document.createElement("div");
            spark.className = "spark";
            spark.style.left = e.clientX + "px";
            spark.style.top = e.clientY + "px";
            document.body.appendChild(spark);

            setTimeout(() => spark.remove(), 800);
        });
        </script>
        """,
        height=800,
        width=2000,
    )
