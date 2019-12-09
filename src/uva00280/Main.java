import java.util.Scanner;
import java.util.StringTokenizer;

class Main {
    private final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Main main = new Main();
        main.run();
    }

    public void run() {
        // Cache para armazenar as linhas que contenham os números de vértices nos grafos.
        String line;

        while ((line = scanner.nextLine()) != null) {
            // Número de vértices no grafo.
            int vertices = Integer.parseInt(line);

            if (vertices == 0) {
                break;
            }

            boolean [][] graph = new boolean [vertices][vertices];

            // Identificando os vértices que possuem arestas direcionadas.
            while (true) {
                StringTokenizer st = new StringTokenizer(scanner.nextLine());
                int verticeSrc = Integer.parseInt(st.nextToken()) - 1;

                // Identificando o fim da definição das arestas direcionadas.
                if (verticeSrc == -1) {
                    break;
                }

                while (st.hasMoreTokens()) {
                    int verticeDest = Integer.parseInt(st.nextToken()) - 1;
                    if (verticeDest == - 1) {
                        break;
                    }

                    // Pegando os vértices de destino e definindo a aresta entre origem e destino como true.
                    graph[verticeSrc][verticeDest] = true;
                }
            }

            // Pegando os vértices para iniciar as buscas.
            StringTokenizer st = new StringTokenizer(scanner.nextLine());
            int verticesResearch = Integer.parseInt(st.nextToken());

            for (int i = 0; i < verticesResearch; i++) {
                // Pegando o vértice inicial para iniciar as buscas.
                int verticeStart = Integer.parseInt(st.nextToken()) - 1;

                Vertex vertex = new Vertex(vertices, graph, verticeStart);
                vertex.solve();

                System.out.println();
            }
        }
    }

    class Vertex {

        int [] inaccessibleVertices;
        boolean [][] graph;
        boolean [] walked;
        int vertices;
        int vertice;
        
        Vertex(int vertices, boolean [][] graph, int vertice) {
            this.walked = new boolean [vertices];
            this.graph = graph;
            this.vertices = vertices;
            this.vertice = vertice;
            // Posição 0 conterá a quantidade de vértices inacessíveis.
            this.inaccessibleVertices = new int [vertices + 1];
        }

        public void solve() {
            // Caminhando através do vértice inicial para mapear os vértices que possui acesso.
            walkGraph(vertice);

            for (int i = 0; i < vertices; i++) {
                if (!walked[i]) {
                    // Contabilizando a quantidade de vértices inacessíveis.
                    inaccessibleVertices[0]++;
                    // Armazenando o número do vértice que é inacessível.
                    inaccessibleVertices[inaccessibleVertices[0]] = i + 1;
                }
            }

            // Imprimindo os vértices que o inicial não acessa.
            for (int i = 0; i <= inaccessibleVertices[0]; i++) {
                System.out.print(inaccessibleVertices[i]);
                if (i < inaccessibleVertices[0]) {
                    System.out.print(" ");
                }
            }
        }

        /**
         * Caminha pelo grafo identificando os vértices acessíveis pelo vértice inicial.
         *
         * @param start Vértice inicial.
         */
        public void walkGraph (int start) {
            for (int i = 0; i < graph.length; i++) {
                if (graph[start][i] && !walked[i]) {
                    // Se o vértice é acessível e ainda não foi sinalizado como caminhado recebe true.
                    walked[i] = true;
                    walkGraph(i);
                }
            }
        }

    }
}
