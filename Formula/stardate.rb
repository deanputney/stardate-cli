class Stardate < Formula
  desc "Command line interface for interacting with Stardate app's transcription files"
  homepage "https://github.com/deanputney/homebrew-stardate-cli"
  url "https://github.com/deanputney/homebrew-stardate-cli/releases/download/v0.0.1/stardate-0.0.1.tar.gz"
  sha256 "929e8f522e3c88297e0f7bd98d185788dc150095d8a67fb43c9ada60a1112c47"

  depends_on "python@3.10"

  def install
    bin.install "stardate.py" => "stardate"
    (prefix/"test_data").install Dir["test_data/*"]
  end

  test do
    system "stardate", "--help"
  end
end
