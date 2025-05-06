class Stardate < Formula
  desc "Command line interface for interacting with transcription files"
  homepage "https://github.com/deanputney/stardate"
  url "https://github.com/deanputney/stardate/releases/download/v1.0.0/stardate-1.0.0.tar.gz"
  sha256 "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"

  depends_on "python@3.9"

  def install
    bin.install "stardate.py" => "stardate"
  end

  test do
    system "stardate", "--help"
  end
end
