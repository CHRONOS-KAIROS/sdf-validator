{
  outputs = { self, nixpkgs }:
  let 
    system =  "x86_64-linux";
    pkgs = import nixpkgs { system = system; };
  in
  {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        poetry
        jq
      ];
    };
  };
}

