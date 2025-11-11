const API_URL = "https://project-root-n045.onrender.com/posts";

const postsList = document.getElementById("postsList");
const postForm = document.getElementById("postForm");
const titleInput = document.getElementById("title");
const contentInput = document.getElementById("content");

// Função para carregar posts do backend
async function loadPosts() {
  try {
    const res = await fetch(API_URL);
    const posts = await res.json();

    // Ordena do mais recente para o mais antigo
    posts.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

    postsList.innerHTML = "";
    posts.forEach((post) => {
      const div = document.createElement("div");
      div.className = "post";
      div.innerHTML = `
        <div class="post-title">${post.title}</div>
        <div class="post-date">${new Date(
          post.created_at
        ).toLocaleString()}</div>
        <div class="post-content">${post.content}</div>
        <button onclick="deletePost(${post.id})">Excluir</button>
      `;
      postsList.appendChild(div);
    });
  } catch (err) {
    console.error("Erro ao carregar posts:", err);
  }
}

// Função para criar post
postForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const newPost = {
    title: titleInput.value,
    content: contentInput.value,
  };

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newPost),
    });

    if (!res.ok) throw new Error("Erro ao criar post");

    titleInput.value = "";
    contentInput.value = "";
    loadPosts(); // Atualiza lista
  } catch (err) {
    console.error(err);
  }
});

// Função para deletar post
async function deletePost(id) {
  try {
    const res = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    if (!res.ok) throw new Error("Erro ao deletar post");
    loadPosts(); // Atualiza lista
  } catch (err) {
    console.error(err);
  }
}

// Carrega posts inicialmente
loadPosts();
