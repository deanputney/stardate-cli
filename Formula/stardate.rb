class Stardate < Formula
  desc "Command line interface for interacting with Stardate app's transcription files"
  homepage "https://github.com/deanputney/stardate-cli"
  url "https://github.com/deanputney/stardate-cli/releases/download/v0.0.1/stardate-0.0.1.tar.gz"
  sha256 "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"

  depends_on "python@3.10"

  def install
    bin.install "stardate.py" => "stardate"
  end

  test do
    system "stardate", "--help"
  end
end
