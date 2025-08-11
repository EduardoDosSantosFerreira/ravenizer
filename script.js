// Função para alternar as perguntas do FAQ
document.querySelectorAll(".faq-question").forEach((question) => {
  question.addEventListener("click", () => {
    const answer = question.nextElementSibling;
    const icon = question.querySelector("i");

    // Alternar a exibição da resposta
    if (answer.style.display === "block") {
      answer.style.display = "none";
      icon.classList.replace("fa-chevron-up", "fa-chevron-down");
    } else {
      answer.style.display = "block";
      icon.classList.replace("fa-chevron-down", "fa-chevron-up");
    }
  });
});

// Inicialmente esconder todas as respostas do FAQ
document.querySelectorAll(".faq-answer").forEach((answer) => {
  answer.style.display = "none";
});

// Animação ao rolar para as seções
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animated");

        // Remover o observer após a animação para melhor performance
        if (entry.target.classList.contains("animated")) {
          observer.unobserve(entry.target);
        }
      }
    });
  },
  {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px", // Dispara a animação 50px antes do elemento entrar na viewport
  }
);

// Observar elementos que devem ser animados
const elementsToAnimate = [
  ...document.querySelectorAll(".section-title"),
  ...document.querySelectorAll(".screenshot"),
  ...document.querySelectorAll(".requirements"),
  ...document.querySelectorAll(".faq-item"),
  document.querySelector("#download p"),
  document.querySelector("#download .download-btn"),
  document.querySelector("#download .version"),
];

elementsToAnimate.forEach((el) => {
  observer.observe(el);
});

// Efeito de hover para os screenshots - versão melhorada
document.querySelectorAll(".screenshot").forEach((screenshot) => {
  screenshot.addEventListener("mouseenter", () => {
    const img = screenshot.querySelector("img");
    img.style.transform = "scale(1.05)";
    screenshot.style.boxShadow = "0 10px 25px rgba(46, 204, 113, 0.3)";
  });

  screenshot.addEventListener("mouseleave", () => {
    const img = screenshot.querySelector("img");
    img.style.transform = "scale(1)";
    screenshot.style.boxShadow = "none";
  });
});

// Simular download (substitua pelo link real)
document
  .getElementById("download-btn-bottom")
  .addEventListener("click", function (e) {
    e.preventDefault();

    // Feedback visual
    const btn = this;
    btn.innerHTML =
      '<i class="fas fa-spinner fa-spin"></i> PREPARANDO DOWNLOAD...';
    btn.style.backgroundColor = "var(--primary-dark)";

    // Simular tempo de preparação
    setTimeout(() => {
      alert(
        "Download iniciado! (Esta é uma demonstração. Substitua pelo link real de download.)"
      );
      btn.innerHTML = '<i class="fas fa-download"></i> BAIXAR AGORA';
      btn.style.backgroundColor = "var(--primary)";

      // Aqui você colocaria o link real:
      // window.location.href = 'URL_DO_SEU_DOWNLOAD_AQUI';
    }, 1500);
  });

// Efeito de rolagem suave para links internos
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const targetId = this.getAttribute("href");
    if (targetId === "#") return;

    const targetElement = document.querySelector(targetId);
    if (targetElement) {
      window.scrollTo({
        top: targetElement.offsetTop - 80,
        behavior: "smooth",
      });
    }
  });
});

// Ativar/desativar animação de pulse nos botões quando visíveis
const pulseObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      const btn = entry.target;
      if (entry.isIntersecting) {
        btn.classList.add("pulse");
      } else {
        btn.classList.remove("pulse");
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll(".download-btn").forEach((btn) => {
  pulseObserver.observe(btn);
});
