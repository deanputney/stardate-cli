class Stardate < Formula
  desc "Command line interface for interacting with Stardate app's transcription files"
  homepage "https://github.com/deanputney/stardate-cli"
  url "https://github.com/deanputney/stardate-cli/releases/download/v0.0.1/stardate-0.0.1.tar.gz"
  sha256 "0986c59232618580a6dec54b035bccdac1521c72000771d9707499f3e0e5c943"

  depends_on "python@3.10"

  def install
    bin.install "stardate.py" => "stardate"
    (prefix/"test_data").install Dir["test_data/*"]
  end

  test do
    system "stardate", "--help"
  end
end
