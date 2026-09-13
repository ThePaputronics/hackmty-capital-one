import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';

export const Scene04Architecture: React.FC = () => {
  const frame = useCurrentFrame();

  const c1 = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const c2 = interpolate(frame, [25, 45], [0, 1], { extrapolateRight: 'clamp' });
  const c3 = interpolate(frame, [50, 70], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        padding: '0 120px',
      }}
    >
      <div style={{ marginBottom: '50px' }}>
        <span style={{ color: theme.colors.accent, fontFamily: theme.fonts.mono, fontSize: '15px', letterSpacing: '3px', textTransform: 'uppercase' }}>
          Arquitectura del Sistema
        </span>
        <h2 style={{ color: theme.colors.textPrimary, fontFamily: theme.fonts.serif, fontSize: '50px', margin: '8px 0 0 0' }}>
          Tres piezas simples. Cero acoplamiento.
        </h2>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '30px' }}>
        {/* Componente 1: Generador */}
        <div
          style={{
            opacity: c1,
            backgroundColor: theme.colors.surface,
            border: `1px solid ${theme.colors.surfaceBorder}`,
            borderRadius: '16px',
            padding: '36px 30px',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <div style={{ color: theme.colors.accent, fontSize: '14px', fontFamily: theme.fonts.mono, marginBottom: '14px' }}>
            01 · SIMULADOR / WORKER
          </div>
          <div style={{ color: '#fff', fontSize: '28px', fontFamily: theme.fonts.serif, fontWeight: 600, marginBottom: '16px' }}>
            Event Stream
          </div>
          <div style={{ color: theme.colors.textSecondary, fontSize: '16px', lineHeight: 1.5 }}>
            Emite eventos bancarios con reloj simulado (90 días de warmup + 30 días de stream activo). No filtra información de ataque al motor.
          </div>
        </div>

        {/* Componente 2: API & Scorers */}
        <div
          style={{
            opacity: c2,
            backgroundColor: '#1b2233',
            border: `2px solid ${theme.colors.accent}`,
            borderRadius: '16px',
            padding: '36px 30px',
            display: 'flex',
            flexDirection: 'column',
            boxShadow: '0 0 30px rgba(216, 155, 66, 0.15)',
          }}
        >
          <div style={{ color: theme.colors.accentLight, fontSize: '14px', fontFamily: theme.fonts.mono, marginBottom: '14px' }}>
            02 · SENTINEL CORE
          </div>
          <div style={{ color: '#fff', fontSize: '28px', fontFamily: theme.fonts.serif, fontWeight: 600, marginBottom: '16px' }}>
            Motor de Corroboración
          </div>
          <div style={{ color: '#c7cddf', fontSize: '16px', lineHeight: 1.5 }}>
            Calcula 3 puntuaciones ortogonales (ATO, Intención, Destinatario). Aplica regla de corroboración multi-factor en &lt; 4ms.
          </div>
        </div>

        {/* Componente 3: UI Dashboard */}
        <div
          style={{
            opacity: c3,
            backgroundColor: theme.colors.surface,
            border: `1px solid ${theme.colors.surfaceBorder}`,
            borderRadius: '16px',
            padding: '36px 30px',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <div style={{ color: theme.colors.accent, fontSize: '14px', fontFamily: theme.fonts.mono, marginBottom: '14px' }}>
            03 · DASHBOARD & OPS
          </div>
          <div style={{ color: '#fff', fontSize: '28px', fontFamily: theme.fonts.serif, fontWeight: 600, marginBottom: '16px' }}>
            Panel Classical UI
          </div>
          <div style={{ color: theme.colors.textSecondary, fontSize: '16px', lineHeight: 1.5 }}>
            Dashboard en tiempo real con cero lógica de negocio. Muestra feed de auditoría, tarjetas de intervención y métricas de fraude evitado.
          </div>
        </div>
      </div>
    </div>
  );
};
