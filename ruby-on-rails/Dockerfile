# syntax=docker/dockerfile:1
FROM ruby:3.3.6-slim

# Basic config
ENV BUNDLE_PATH=/usr/local/bundle \
    RAILS_ENV=development \
    TZ=America/Chicago

WORKDIR /app

# OS packages – just the essentials
RUN apt-get update -qq && \
    apt-get install --no-install-recommends -y build-essential libsqlite3-dev nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install Rails (and Bundler is already included in the Ruby image)
RUN gem install rails -v "~> 7.1.2" --no-document

# Tiny entrypoint that can generate the app on first run
COPY bin/docker-entrypoint /usr/bin/entrypoint
RUN chmod +x /usr/bin/entrypoint

EXPOSE 3000
ENTRYPOINT ["entrypoint"]
CMD ["rails", "server", "-b", "0.0.0.0"]
