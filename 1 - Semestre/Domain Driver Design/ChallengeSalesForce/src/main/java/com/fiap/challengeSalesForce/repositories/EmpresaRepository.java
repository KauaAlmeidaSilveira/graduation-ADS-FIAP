package com.fiap.challengeSalesForce.repositories;

import com.fiap.challengeSalesForce.entities.Empresa;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmpresaRepository extends JpaRepository<Empresa, Long> {
}
