{
  description = "Python Profiling Demo - A TUI application for demonstrating profiling techniques";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        
        # Python 3.13 with required packages
        python = pkgs.python313;
        
        pythonEnv = python.withPackages (ps: with ps; [
          rich
          pip
        ]);
        
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pythonEnv
            pkgs.valgrind
            pkgs.graphviz
            # snakeviz will be installed via pip in the shell
          ];
          
          shellHook = ''
            echo "🐍 Python Profiling Demo Environment"
            echo "====================================="
            echo ""
            echo "Python version: $(python --version)"
            echo ""
            
            # Install snakeviz if not already installed
            if ! python -c "import snakeviz" 2>/dev/null; then
              echo "📦 Installing snakeviz..."
              pip install --user snakeviz 2>/dev/null
            fi
            
            echo "Available tools:"
            echo "  • python        - Python 3.13"
            echo "  • valgrind      - Memory profiling"
            echo "  • snakeviz      - Profile visualization"
            echo "  • dot/graphviz  - Graph visualization"
            echo ""
            echo "Quick start:"
            echo "  python profiler_demo.py    - Run the TUI application"
            echo ""
            echo "See README.md for detailed usage instructions"
            echo ""
          '';
        };
        
        # Default package - the demo script
        packages.default = pkgs.writeShellScriptBin "profiler-demo" ''
          ${pythonEnv}/bin/python ${./profiler_demo.py}
        '';
        
        # App definition for `nix run`
        apps.default = {
          type = "app";
          program = "${self.packages.${system}.default}/bin/profiler-demo";
        };
      }
    );
}
