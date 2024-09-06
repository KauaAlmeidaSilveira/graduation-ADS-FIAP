package br.com.javamysql.repository;

import br.com.javamysql.entity.Word;
import org.springframework.data.domain.Page;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface WordRepository extends JpaRepository<Word, Long> {

    @Query("""
           FROM Word w WHERE
           LOWER(w.word) LIKE %searchTerm%
           """)
    Page<Word> search(String searchTerm);

}
